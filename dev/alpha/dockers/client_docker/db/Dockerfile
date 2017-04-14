FROM postgres:9.6
COPY docker-entrypoint2.sh /usr/local/bin/
RUN ln -s usr/local/bin/docker-entrypoint2.sh / # backwards compat
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 5432
CMD ["postgres"]