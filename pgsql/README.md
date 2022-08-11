# PostegreSQL schemas

## Prerequisites
1. install dependencies with `pip install -r requirements.txt`

## Migrating the Database:

1. Modify schemas in the `models/` directory
2. Optionally, set the `MIGRATION_POSTGRES_URL` to a non-local DB url to migration scripts based on it
3. Run the following command to generate the migration scripts
    `alembic revision --autogenerate -m "Adds/modify some schema..."`
4. Review the generated scripts in `alembic/versions` to make sure they are correct
5. Try your migration locally with `alembic upgrade head`
    * to change the generated migration script after modifying models:
        * if the migration succeeded, downgrade with `alembic downgrade -1`
        * restart from step 1
    * see the documentation to use alembic: https://alembic.sqlalchemy.org/en/latest/tutorial.html
6. When it works, push all changes in a single commit
