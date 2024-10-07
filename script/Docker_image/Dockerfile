FROM php:8.2-fpm-alpine

# Install necessary PHP extensions
RUN apk add --no-cache \
    php-pdo_mysql \
    php-mysqli \
    php-curl \
    php-gd \
    php-zip \
    php-mbstring \
    php-openssl \
    php-bcmath

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Copy your Laravel project
COPY . /var/www/html

# Set the working directory
WORKDIR /var/www/html

# Install Laravel dependencies
RUN composer install

# Expose the web server port
EXPOSE 80

# Define the command to run when the container starts
CMD ["php-fpm"]

-------------------
FROM php:8.2-fpm-alpine

# Install necessary PHP extensions
RUN apk add --no-cache \
    php-pdo_mysql \
    php-mysqli \
    php-curl \
    php-gd \
    php-zip \
    php-mbstring \
    php-openssl \
    php-bcmath

# Install Composer
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer

# Copy your Laravel project
COPY . /var/www/html

# Set the working directory
WORKDIR /var/www/html

# Install Laravel dependencies
RUN composer install

# Make the test.php file executable
RUN chmod +x /var/www/html/test.php

# Expose the web server port
EXPOSE 80

# Define the command to run when the container starts
CMD ["php-fpm"]
