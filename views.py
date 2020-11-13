from django.shortcuts import render
from appPro.models import Sucursal, Marca, Categoria, Producto
#from gestorDeProducto.models import *

# Create your views here.
def plantilla(request):
	return render(request, 'plantillaBase.html', {} )
	
def registro(request):
	nombre = ""
	
	if request.method == "POST":
		nombre = request.POST["txtNombre"]
		

	contexto = {'nombre': nombre, 'valor1' : 135234, 'valor2': 6546}
	return render(request, 'registro.html', contexto )
	
def productos(request):
	return render(request, 'productos.html', {} )
	
	
def sucursal(request):
	mensaje = ""
	lista 	= {}
	item 	= {}
	if request.method == "POST": # verifica si existe una solicitud
		#validar los datos antes guardar
		id	 		= int("0" + request.POST["txtId"])
		nombre 		= request.POST["txtNombre"]
		direccion 	= request.POST["txtDireccion"]
		telefono	= request.POST["txtTelefono"]
		encargado	= request.POST["txtEncargado"]

		if 'btnGrabar' in request.POST:
			if id < 1:
				Sucursal.objects.create(nombre=nombre, direccion=direccion, telefono=telefono, encargado=encargado)
			else:
				item = Sucursal.objects.get(pk = id)
				item.nombre 	= nombre
				item.direccion 	= direccion
				item.telefono 	= telefono
				item.encargado 	= encargado
				item.save()
				item = {}
			
			mensaje = "La operación realizada con éxito"
		elif 'btnListar' in request.POST:
			# lista = Sucursal.objects.all()	# como filtrar los datos de un modelo (ORM)	
			lista = Sucursal.objects.filter(nombre__contains = nombre)
		elif 'btnBuscar' in request.POST:
			item = Sucursal.objects.get(pk = id)
		elif 'btnEliminar' in request.POST:
			item = Sucursal.objects.get(pk = id)
			item.delete()
			mensaje = "El registro " + item.nombre +" fue eliminado"			
			item = {}

	contexto = {'mensaje' : mensaje, 'lista' : lista, 'item' : item}
	return render(request, 'sucursal.html', contexto )
	
	
def producto(request):
	mensaje 	= ""
	lista 		= {}
	item 		= {}
	cmbMarca 	= Marca.objects.filter(activo = True)
	cmbCategoria= Categoria.objects.filter(activo = True)
	errores		= {}
	
	if request.method == "POST": # verifica si existe una solicitud
		#validar los datos antes guardar
		id	 		= int("0" + request.POST["txtId"])
		idMarca		= int("0" + request.POST["cmbMarca"])
		idCategoria	= int("0" + request.POST["cmbCategoria"])
		codigo 		= int("0" + request.POST["txtCodigo"])
		descripcion = request.POST["txtDescripcion"]
		stock 		= int("0" + request.POST["txtStock"])
		precioCosto = int("0" + request.POST["txtPrecioCosto"])
		precioVenta = int("0" + request.POST["txtPrecioVenta"])

		if 'btnGrabar' in request.POST:
			marca 		= buscarPorId(Marca, idMarca)
			categoria 	= buscarPorId(Categoria, idCategoria)	
			
			if marca is None:
				errores['cmbMarca'] = "No seleccionó la marca"
			elif categoria is None:
				errores['cmbCategoria'] = "No seleccionó la categoria"			
			else:
				if id < 1:		
					Producto.objects.create(marca=marca, categoria=categoria, codigo=codigo,descripcion=descripcion,stock=stock,precioCosto=precioCosto,precioVenta=precioVenta)
					mensaje = "El producto fue guardado con éxito"
				else:
					item 			= Producto.objects.get(pk = id)
					item.marca 		= marca
					item.codigo 	= codigo
					item.descripcion= descripcion
					item.stock 		= stock
					item.precioCosto= precioCosto
					item.precioVenta= precioVenta
					item.save()
					item = {}			
					mensaje = "La operación realizada con éxito"
		elif 'btnListar' in request.POST:
			# lista = Sucursal.objects.all()	# como filtrar los datos de un modelo (ORM)	
			lista = Producto.objects.filter(descripcion__contains = descripcion)
		elif 'btnBuscar' in request.POST:
			item = Producto.objects.get(pk = id)
		elif 'btnEliminar' in request.POST:
			item = Producto.objects.get(pk = id)
			item.delete()
			mensaje = "El registro " + item.nombre +" fue eliminado"			
			item = {}

	contexto = {'mensaje' : mensaje, 'lista' : lista, 'item' : item, 'cmbMarca':cmbMarca, 'cmbCategoria':cmbCategoria, 'errores':errores}
	return render(request, 'producto.html', contexto )

def buscarPorId(modelo, pk):
	try:
		objeto = modelo.objects.get(pk = pk)
	except:
		objeto = None
	return objeto