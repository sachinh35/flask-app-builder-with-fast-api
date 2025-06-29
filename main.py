from fastapi import FastAPI
from a2wsgi import WSGIMiddleware
import uvicorn
from fab_app import app as flask_app, db as fab_db, app_builder as fab_app_builder

fastapi_app = FastAPI(
    title="FastAPI with Flask-AppBuilder",
    description="An example of mounting a Flask-AppBuilder app into FastAPI.",
    version="1.0.0",
)


@fastapi_app.get("/")
async def read_root():
    return {"message": "Hello from FastAPI!"}


@fastapi_app.get("/fastapi-info")
async def fastapi_info():
    return {"fastapi_status": "Operational", "framework": "FastAPI"}


# Mount Flask-AppBuilder app at '/fab' path
fastapi_app.mount("/fab", WSGIMiddleware(flask_app), name="flask_appbuilder")


@fastapi_app.on_event("startup")
def create_db_and_tables():
    with flask_app.app_context():
        fab_db.create_all()

        sm = fab_app_builder.sm

        admin_role = sm.find_role('Admin')
        if not admin_role:
            admin_role = sm.add_role('Admin')
            fab_db.session.commit()
            print("Admin role created.")

        if not sm.find_user(username='admin'):
            sm.add_user(
                username='admin',
                first_name='Admin',
                last_name='User',
                email='admin@example.com',
                role=admin_role,
                password='admin',
            )
            fab_db.session.commit()
            print("Admin user created.")
        else:
            print("Admin user already exists.")

        print("Database and Flask-AppBuilder initialized!")


if __name__ == "__main__":
    uvicorn.run(fastapi_app, host="0.0.0.0", port=8000)
