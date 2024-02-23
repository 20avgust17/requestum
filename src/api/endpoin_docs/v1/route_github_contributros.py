GET_DATA_LIFETIME_RESPONSES = {
    422: {
        'description': 'URL must be from GitHub domain',
        'content': {
            'application/json': {
                'example': {
                    'detail': "1 validation error for GitHubUrl\ngithub_url\n  URL must be from GitHub domain \
                    (type=value_error)"
                }
            }
        }
    }
}
