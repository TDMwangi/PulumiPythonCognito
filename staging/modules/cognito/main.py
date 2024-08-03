import pulumi_aws as aws


def cognito_user_pool():
    user_pool = aws.cognito.UserPool(
        "tdm_user_pool",
        name="tdm-user-pool",
        deletion_protection="INACTIVE",
        auto_verified_attributes=["email"],

        user_attribute_update_settings=aws.cognito.UserPoolUserAttributeUpdateSettingsArgs(
            attributes_require_verification_before_updates=["email"]
        ),

        account_recovery_setting=aws.cognito.UserPoolAccountRecoverySettingArgs(
            recovery_mechanisms=[
                aws.cognito.UserPoolAccountRecoverySettingRecoveryMechanismArgs(
                    name="verified_email",
                    priority=1
                )
            ]
        ),

        email_configuration=aws.cognito.UserPoolEmailConfigurationArgs(
            email_sending_account="COGNITO_DEFAULT"
        ),

        password_policy=aws.cognito.UserPoolPasswordPolicyArgs(
            minimum_length=8,
            require_lowercase=True,
            require_uppercase=True,
            require_numbers=True,
            require_symbols=True,
            temporary_password_validity_days=7
        )
    )

    aws.cognito.UserPoolClient(
        "tdm_app_client",
        name="tdm-app-client",
        user_pool_id=user_pool.id,
        access_token_validity=24,
        generate_secret=True,
        enable_token_revocation=True,

        explicit_auth_flows=[
            "ALLOW_REFRESH_TOKEN_AUTH",
            "ALLOW_USER_PASSWORD_AUTH",
            "ALLOW_USER_SRP_AUTH"
        ]
    )
