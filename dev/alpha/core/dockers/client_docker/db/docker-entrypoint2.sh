#!/bin/sh
set -e

echo
echo test
echo

psql --username postgres <<-EOSQL
	CREATE DATABASE client_db ;
EOSQL
echo

echo
echo end test
echo