FROM php:8.2-fpm-alpine

# Create non-root user
RUN addgroup -g 82 -S appgroup && adduser -u 82 -S appuser -G appgroup

WORKDIR /var/www/html
COPY index.php .
RUN chown -R appuser:appgroup /var/www/html

USER appuser
EXPOSE 9000
CMD ["php-fpm"]