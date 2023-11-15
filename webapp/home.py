import justpy as jp

class Home:
	path = "/"

	def serve(self):
		wp = jp.QuasarPage(tailwind=True)
		div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
		jp.Div(a=div, text="This is the Home page!", classes="text-4xl m-2")
		jp.Div(a=div, text="""
				Caelum serenum et tranquillum est, ubi sol splendet et 
				nubes absent. In horto floribus coloratis et arboribus 
				frondosis, amici mei et ego ambulamus. Sub arbore, 
				volumina scripta legimus et philosophiam discimus. 
				Tempus fugit, sed amicitia aeternum manet. 
				Veritas et iustitia nobiscum sunt, 
				et in corde nostro spes floret. Vita est donum divinum, 
				et gratias agimus pro omnibus momentis. 
				In medio difficilium temporum, spem retinemus et perseveramus. 
				Carpe diem, quam minimum credula postero. 
				Amor et pax sint in cordibus omnium hominum.
				""", classes="text-lg")
		return wp