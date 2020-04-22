.PHONY: build test push run

PKGNAME := tonyzhang/ioc-app-for-allison:dev

build:
	docker build --no-cache -t $(PKGNAME) .

push:
	# docker tag ioc:dev tonyzhang/ioc-test:dev
	docker push $(PKGNAME)

test:
	docker run --rm -it $(PKGNAME) bash

run:
	docker run --rm -it --name myIOCAppAS $(PKGNAME)
