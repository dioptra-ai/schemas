# PostegreSQL schemas

## Prerequisites
1. install dependencies with `pip install -r requirements.txt`

## Migrating the Database:

1. Modify schemas in the `models/` directory
1. Run the following command to generate the migration scripts
    `alembic revision --autogenerate -m "Adds/modify some schema..."`
1. Review the generated scripts in `alembic/versions` to make sure they are correct
1. Try your migration locally with `alembic upgrade head`
    * to change the generated migration script after modifying models:
        * if the migration succeeded, downgrade with `alembic downgrade -1`
        * restart from step 1
    * see the documentation to use alembic: https://alembic.sqlalchemy.org/en/latest/tutorial.html
1. When it works, push all changes in a single commit
