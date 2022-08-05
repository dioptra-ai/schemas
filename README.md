# Schemas

Once the schemas are modified

1. run the following command to generate the migration scripts
    `alembic revision --autogenerate -m "Adds/modify some schema..."`
1. review the generated scripts in `alembic/versions` to make sure they are correct
1. try your migration locally with `alembic upgrade head`
    * to change the generated migration script after modifying models:
        * if the migration succeeded, downgrade with `alembic downgrade -1`
        * modify the file
        * re-run `alembic upgrade head`
    * see the documentation to use alembic: https://alembic.sqlalchemy.org/en/latest/tutorial.html
1. when it works, push all changes in a single commit
