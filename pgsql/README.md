# PostegreSQL schemas

## Development Prerequisites
1. Locally install the dependencies with `source .venv/bin/activate && pip install -r requirements.txt`

## Creating a New Migration
1. Modify schemas in the `models/` or `functions/` directory
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

> Check current revision of an RDS Database
> DANGEROUS TRICK: YOU'RE LIKELY TO FORGET TO UNSET `MIGRATION_POSTGRES_URL` AND RUN `alembic upgrade head` ON A PRODUCTION DB.
> 1. Port-forward an RDS db with this script https://github.com/dioptra-ai/dioptra/blob/dev/script/port-forward-rds.sh
> 1. Set the `MIGRATION_POSTGRES_URL` env variable to a non-local DB url: `export MIGRATION_POSTGRES_URL=postgresql://postgres:<passwd>@localhost:5432/dioptra`
> 1. Check the current revision of that DB with `alembic current; unset MIGRATION_POSTGRES_URL`
> 1. DON'T FORGET `unset MIGRATION_POSTGRES_URL`
