#include <stdlib.h>
#include <epicsExport.h>
#include <dbAccess.h>
#include <devSup.h>
#include <recSup.h>
#include <recGbl.h>
#include <callback.h>
#include <math.h>

#include <aiRecord.h>

long frand_r(unsigned int*);

static long init_record(aiRecord *pao);
static long read_ai(aiRecord *pao);

struct prngState {
    unsigned int seed;
    CALLBACK cb;
};

struct {
    long num;
    DEVSUPFUN report;
    DEVSUPFUN init;
    DEVSUPFUN init_record;
    DEVSUPFUN get_ioint_info;
    DEVSUPFUN read_ai;
    DEVSUPFUN special_linconv;
} devAiPrngAsync = {
    6,
    NULL,
    NULL,
    init_record,
    NULL,
    read_ai,
    NULL
};
epicsExportAddress(dset, devAiPrngAsync);

void prng_cb(CALLBACK* cb);

static long init_record(aiRecord *pao)
{
    struct prngState* priv;
    unsigned long start;

    priv = malloc(sizeof(struct prngState));
    if (!priv) {
        recGblRecordError(S_db_noMemory, (void*)pao,
                "devAoTimebase failed to allocate private struct");
        return S_db_noMemory;
    }

    callbackSetCallback(prng_cb, &priv->cb);
    callbackSetPriority(priorityLow, &priv->cb);
    callbackSetUser(pao, &priv->cb);
    priv->cb.timer = NULL;

    recGblInitConstantLink(&pao->inp, DBF_ULONG, &start);

    priv->seed = start;
    pao->dpvt = priv;

    return 0;
}

static long read_ai(aiRecord *pao)
{
    struct prngState* priv = pao->dpvt;
    if(! pao->pact) {
        pao->pact = TRUE;
        callbackSetUser(pao, &priv->cb);
        callbackRequestDelayed(&priv->cb, 0.1);
        return 0;
    } else {
        pao->pact = FALSE;
        return 0;
    }
}

void prng_cb(CALLBACK* cb)
{
    aiRecord* prec;
    struct prngState* priv;
    struct rset* prset;
    epicsInt32 raw;

    callbackGetUser(prec, cb);
    prset = (struct rset*) prec->rset;
    priv = prec->dpvt;

    raw = frand_r(&priv->seed);

    dbScanLock((dbCommon*)prec);
    prec->rval = raw;
    (*prset->process)(prec);
    dbScanUnlock((dbCommon*)prec);
}

long fac(int n)
{
    if(n==0 || n<0)
        return 1;
    long f = 1;
    for(int i=1; i<=n; ++i)
    {
        f *= i;
    }
    return f;
}

long frand_r(unsigned int* seed)
{
    long n = rand_r(seed);
    int r = n % 100 + 50;
    //printf("%d", fac(r));
    return fac(r) % (int)1e9;
}
