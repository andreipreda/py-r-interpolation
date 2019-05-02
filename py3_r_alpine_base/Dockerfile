FROM alpine:edge

# --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted
RUN apk add --no-cache ca-certificates

# general libraries used
RUN apk add --no-cache --update-cache gcc gfortran py-pip build-base wget freetype-dev libpng-dev openblas-dev

# python 3.7+ (from the edge alpine above at 30th April)
RUN apk add --no-cache python3 python3-dev

# openblas for R as well (checked & working)

### ps aux (found R session)
### lsof -p PID_FOUND | grep 'blas'
### / # lsof -p 73 | grep 'blas'
### R  PID root  mem    REG    8,1 28402664  398085 /usr/lib/libopenblasp-r0.3.3.so
RUN apk add --no-cache R R-dev R-mathlib

# for rpy2 foreign language prototol
RUN apk add --no-cache libffi libffi-dev

# R home for rpy2
ENV R_HOME=/usr/lib/R
# R libs path
ENV LD_LIBRARY_PATH=/usr/lib/R/lib
