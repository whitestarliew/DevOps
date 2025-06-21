FROM nginxinc/nginx-unprivileged:stable-alpine

WORKDIR /usr/share/nginx/html
COPY default.conf /etc/nginx/conf.d/default.conf

ENV NGINX_LOG_LEVEL=info

HEALTHCHECK --interval=30s --timeout=3s CMD curl -f http://localhost:8080 || exit 1

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["nginx", "-g", "daemon off;"]
