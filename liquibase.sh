#!/bin/sh

liquibase_update()
{
  docker run --rm \
-v "$(pwd)/db:/liquibase/db" \
--network="host" \
--user 1000 \
liquibase/liquibase  \
--url="jdbc:postgresql://127.0.0.1:5443/staff-planning" \
--username=staff-planning \
--password=staff-planning \
--changeLogFile=db/master.xml \
update
}

if [ "$1" = "update" ] ; then
    liquibase_update
else
      liquibase_update
fi

