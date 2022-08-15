# PostegreSQL schemas

## Development Prerequisites
1. Locally install the dependencies with `pip install -r requirements.txt`

## Creating a New Migration
1. Modify schemas in the `models/` or `functions/` directory
2. Optionally, set the `MIGRATION_POSTGRES_URL` env variable to a non-local DB url to generate scripts based on the state of that DB (see how to port-forward an RDS db here: https://github.com/dioptra-ai/dioptra/blob/dev/script/port-forward-rds.sh)
3. Run the following command to generate the migration scripts
    `alembic revision --autogenerate -m "Adds/modify some schema..."`
4. Review the generated scripts in `alembic/versions` to make sure they are correct and add any data migration
5. ***If you set `MIGRATION_POSTGRES_URL`, unset it to avoid migrating a non-local DB.*** 
6. Try your migration locally: `alembic upgrade head`. 
7. Iterate on the migration:
    * if the migration succeeded, downgrade with `alembic downgrade -1`
    * restart from step 1
    * see the documentation to use alembic: https://alembic.sqlalchemy.org/en/latest/tutorial.html
8. When it works, push all changes in a single commit
