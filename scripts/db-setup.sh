#!/bin/sh

export PGUSER="postgres"

psql -c "CREATE DATABASE inventory"

psql inventory -c "CREATE EXTENSIONS IF NOT EXISTS \"uuid-ossp\";"
