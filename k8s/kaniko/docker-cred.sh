kubectl -n jenkins delete secret regcred
kubectl -n jenkins create secret docker-registry regcred --docker-server=https://index.docker.io/v1/  \
--docker-username=skmaifujalam --docker-password=Newman123@ --docker-email=sk.maifujalam@gmail.com
