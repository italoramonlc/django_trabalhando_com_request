import json

from django.shortcuts import redirect
from django.http import HttpResponse,HttpRequest,HttpResponseRedirect,JsonResponse,FileResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def home(request:HttpRequest) -> FileResponse:
    #trabalhando com arquivos
    return FileResponse(open('relatorio.pdf', 'rb'), as_attachment=True,filename="outro.pdf")
    # with open("RELATORIO.pdf","rb") as file:
    #     return HttpResponse(
    #         content=file.read(),
    #         content_type="application/pdf",
    #         headers={"Content-Disposition":"attachment;filename='relatorio.pdf'"}
    #     )




    #json
    #body = json.dumps({"nome":"Italo","sobrenome":"Cunha"})
    #return HttpResponse(content=body,content_type="application/json",charset="utf-8")
    # body = [
    #     {"nome":"cunha","sobrenome":"lima"},
    #     {"nome":"ana","sobrenome":"souza"},
    #     {"nome":"elton","sobrenome":"pinto"}
    # ]
    # return JsonResponse(body,safe=False)

    # return HttpResponseRedirect("http://localhost:8000/outra-rota")
    # return redirect("outra_rota")
    # if request.method == "GET":
    #     return HttpResponse("<h1>Tudo certo!</h1>")
    # return HttpResponseNotAllowed(permitted_methods=["GET"])


def outra_view(request:HttpRequest) -> HttpResponse:
    return HttpResponse(content="<h1>Outra rota</h1>")






    # body = loader.render_to_string("app/home.html",context=None,request=request)
    # template = loader.get_template("app/home.html")
    # body = template.render(context=None,request=request)
    # print(f"Path:{request.path}")
    # print(f"Path info:{request.path_info}")
    # print(f"Methed:{request.method}")
    # print(f"Content type:{request.content_type}")
    # print(f"Header:{request.headers}")
    # # print(f"Meta:{request.META}")
    # print(f"Session:{request.session.items()}")
    # print(f"User:{request.user.is_superuser}")
    # print(f"Host:{request.get_host()}")
    # print(f"Post:{request.get_port()}")
    # print(f"Full Path:{request.get_full_path()}")
    # print(f"Full Path info{request.get_full_path_info()}")
    # print(f"Is secure:{request.is_secure()}")
    # print(f"Accepts:{request.accepts('application/json')}")
    # print(f"GET:{request.GET}")
    # print(f"POST:{request.POST}")
    # #trabalhando com json
    # body_dict = json.loads(request.body)
    # print(body_dict)

