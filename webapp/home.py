import justpy as jp

class Home:
	path = "/"
	@classmethod
	def serve(cls, req):
		wp = jp.QuasarPage(tailwind=True)

		layout = jp.QLayout(a=wp, view="hHh lpR fFf")
		header = jp.QHeader(a=layout)
		toolbar = jp.QToolbar(a=header)

		drawer = jp.QDrawer(a=layout, show_if_above=True, v_model="left",bordered=True)
		scroller = jp.QScrollArea(a=drawer, classes="fit")
		qlist = jp.QList(a=scroller)
		a_classes = "p-2 m-2 test-lg text-blue-400 hover:text-blue-700"
		jp.A(a=qlist, text="Home", href="/home", classes=a_classes)
		jp.Br(a=qlist)
		jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
		jp.Br(a=qlist)
		jp.A(a=qlist, text="about", href="/about", classes=a_classes)
		jp.Br(a=qlist)

		jp.QBtn(a=toolbar, dense=True, flat=True, round=True, icon="menu",
				click=cls.move_drawer, drawer=drawer)

		jp.QToolbarTitle(a=toolbar, text="Instant Dictionary")

		container = jp.QPageContainer(a=layout)

		div = jp.Div(a=container, classes="bg-gray-200 h-screen")
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

	@staticmethod
	def move_drawer(widget, msg):
		if widget.drawer.value:
			widget.drawer.value = False
		else:
			widget.drawer.value = True

