from flask_restplus_patched import ModelSchema

from .models import Team


class BaseTeamSchema(ModelSchema):

    class Meta:
        model = Team
        fields = (
            Team.id.key,
            Team.title.key,
        )
        dump_only = (
            Team.id.key,
        )


class DetailedTeamSchema(BaseTeamSchema):

    class Meta(BaseTeamSchema.Meta):
        fields = BaseTeamSchema.Meta.fields + (
            Team.members.key,
            Team.created.key,
            Team.updated.key,
        )