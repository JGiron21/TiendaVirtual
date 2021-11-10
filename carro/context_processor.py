def importe_total_carro(request):
    total=00.0
    if 'carro' in request.session:
        for key, value in request.session["carro"].items():
            pass
            total=total+(float(value["precio"])*value["cantidad"])
    return {"importe_total_carro":total}