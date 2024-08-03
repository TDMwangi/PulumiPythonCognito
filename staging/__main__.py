from modules.cognito.main import cognito_user_pool

service_init = [
    cognito_user_pool
]


if __name__ == "__main__":
    for service in service_init:
        service()
