from marshmallow import fields, ValidationError


def validate_access_token_master_level(access_token):
    pass
    # user_id, _ = OauthAccessTokens.authenticate(access_token)
    # user_label = User.get_group_label(user_id)
    # if user_label not in ('admin', 'master'):
    #    raise ValidationError(GIVEN_USER_HAS_NOT_THE_REQUIRED_LEVEL)

TOKEN_AUTH = {
    'token': fields.Str(required=True),
}


CREATE_USER = {
    'nome': fields.Str(required=True),
    'email': fields.Str(required=True),
    'password': fields.Str(required=True),
    'pontos': fields.Str(required=False),
    'tipo_user': fields.Str(required=False),
    # 'acess_token': fields.Str(required=True, validate=validate_access_token_master_level),
}


GET_USER = {
    'id_user': fields.Str(required=True),
    # 'acess_token': fields.Str(required=True, validate=validate_access_token_master_level),
}


LOGIN_USER = {
    'email': fields.Str(required=True),
    'password': fields.Str(required=True),
    # 'acess_token': fields.Str(required=True, validate=validate_access_token_master_level),
}


CHANGE_USER = {
    'id_user': fields.Str(required=True),
    'nome': fields.Str(required=False),
    'email': fields.Str(required=False),
    'password': fields.Str(required=False),
    'pontos': fields.Str(required=False),
    'tipo_user': fields.Str(required=False),
    # 'acess_token': fields.Str(required=True, validate=validate_access_token_master_level),
}

# ===============================================================================

CREATE_ITEM = {
    'nome': fields.Str(required=True),
    'material': fields.Str(required=True),
    'peso': fields.Str(required=True),
    'pontos': fields.Str(required=False),
    # 'acess_token': fields.Str(required=True, validate=validate_access_token_master_level),
}


GET_ITEM = {
    'id_item': fields.Str(required=True),
    # 'acess_token': fields.Str(required=True, validate=validate_access_token_master_level),
}

# ===============================================================================

CREATE_LIXEIRA = {
    'enderesso_fisico': fields.Str(required=True),
    'capacidade': fields.Str(required=False),
    'status': fields.Str(required=False),
    # 'acess_token': fields.Str(required=True, validate=validate_access_token_master_level),
}


GET_LIXEIRA = {
    'id_lixeira': fields.Str(required=True),
    # 'acess_token': fields.Str(required=True, validate=validate_access_token_master_level),
}


UPDATE_LIXEIRA_CAPACIDADE = {
    'id_lixeira': fields.Str(required=True),
    'capacidade': fields.Str(required=True),
    # 'acess_token': fields.Str(required=True, validate=validate_access_token_master_level),
}
