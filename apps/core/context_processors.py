from django.conf import settings

PROJECT_NAME = "ArtiNo"

def project_context(request):
    return {
        "project_name" : f"{PROJECT_NAME}",
        "project_description" : f"The largest shopping site in the world.",
        "project_keywords" : f"{PROJECT_NAME}, store, shop",
        "project_author" : f"Artin Nobahari",
        "project_color" : f"",
        "project_url" : f"https:www.{PROJECT_NAME}.com",
        "project_cover" : f"https:www.{PROJECT_NAME}.com/static/images/cover.jpg",
        "project_email": f"{PROJECT_NAME}@{PROJECT_NAME}.com",
        "project_phone": f"+98 912 777 77 77",
    }