import detectlanguage

detectlanguage.configuration.api_key = "609c401c57d4180ddbf29d57ad9b273c"
print(detectlanguage.detect("Buenos dias señor"))
print(detectlanguage.simple_detect("तक को बनाया स्टार"))
print(detectlanguage.user_status())
