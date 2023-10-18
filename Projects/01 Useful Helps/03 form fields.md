# Form fields

When you create a Form class, the most important part is defining the fields of the form. Each field has custom validation logic, along with a few other hooks.


## Core field arguments

- required
- label
- label_suffix
- initial
- widget
- help_text
- error_messages
- validators
- localize
- disabled


## Built-in Field classes:

- BooleanField
- CharField
- ChoiceField
- DateField
- DateTimeField
- DecimalField
- DurationField
- EmailField
- FileField
- FilePathField
- FloatField
- GenericIPAddressField
- ImageField
- IntegerField
- JSONField
- MultipleChoiceField
- NullBooleanField
- RegexField
- SlugField
- TimeField
- TypedChoiceField
- TypedMultipleChoiceField
- URLField
- UUIDField
- Slightly complex built-in Field classes
- ComboField
- MultiValueField
- SplitDateTimeField
- Fields which handle relationships
- ModelChoiceField
- ModelMultipleChoiceField
- Iterating relationship choices
- ModelChoiceIterator
- ModelChoiceIteratorValue
- Creating custom fields


## Source link
[Django Form Fields Documentation](https://docs.djangoproject.com/en/4.2/ref/forms/fields/)