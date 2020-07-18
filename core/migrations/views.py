from django.shortcuts import render
html_base = """
    <h1>Mi Primer Menu</h1>
    <ul>
        <li>   <a href="/">Portada</a>              </li>
        <li>   <a href="/about-me/">Acerca de</a>   </li>
        <li>   <a href="/contact/">Contacto</a>     </li>
    </ul>
"""

def home(request, plantilla="home.htlm"):
    return render(request, plantilla)

def about(request, plantilla="about.htlm"):
    return render(request, plantilla)

def contact(request, plantilla="contact.htlm"):
    return render(request, plantilla)


def home (request):
    htlm_responsde= "<h1> la pagina de portada </h1>"
    htlm_responsde = html_base + htlm_responsde
    return HttpResposnde(htlm_responsde),

def contact (request):
    htlm_responsde= "<h1> la pagina de contacto </h1>"
    htlm_responsde = html_base + htlm_responsde
    return HttpResposnde(htlm_responsde),

def about (request):
    htlm_responsde= "<h1> la pagina de Acerca de mi </h1>"
    htlm_responsde = html_base + htlm_responsde
    return HttpResposnde(htlm_responsde),




