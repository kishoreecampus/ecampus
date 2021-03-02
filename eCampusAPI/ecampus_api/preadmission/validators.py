from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.contrib.auth.validators import UnicodeUsernameValidator

class CustomizeMinLengthValidator(MinLengthValidator):
	message = _("Enter at least %(limit_value)d characters")

class CustomizeMaxLengthValidator(MaxLengthValidator):
	message = _("Entered characters exceeds the maximum length (%(limit_value)d)")

class CustomizeUncodeUsernameValidator(UnicodeUsernameValidator):
	regex = r'^[\w._]+\Z'
	message = _("Enter a valid username. This field contain only letters, numbers, and ./_ characters")
