from fastapi import FastAPI
from fastapi_jsonapi import ApplicationBuilder


def build_jsonapi_app(app: FastAPI) -> ApplicationBuilder:
    builder = ApplicationBuilder(app=app)
    builder.add_resource(
        path="/movies",
        tags=["Movies"],
        resource_type="movie",
        view=view,
        model=model,
        schema=schema,
        router=router,
        schema_in_post=schema_in_post,
        schema_in_patch=schema_in_patch,
        pagination_default_size=pagination_default_size,
        pagination_default_number=pagination_default_number,
        pagination_default_offset=pagination_default_offset,
        pagination_default_limit=pagination_default_limit,
        operations=operations,
        ending_slash=ending_slash,
        model_id_field_name=model_id_field_name,
        include_router_kwargs=include_router_kwargs,
    )
    return builder
