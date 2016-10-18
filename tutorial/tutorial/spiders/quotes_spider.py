import scrapy

# class Producto:
#     name = ""
#     price = 0.00
#     image = ""

class QuotesSpider(scrapy.Spider):
    name = "croketero"
    start_urls = [
        'http://www.maskota.com.mx/alimento-para-perro-royal-canin-bulldog-puppy-13-6-kg/p',
        'https://www.petco.com.mx/petco/en/MARCAS/Royal-Canin/Royal-Canin-Labrador-Para-Cachorro/p/BP_104859',
        ]
    def parse(self, response):
        print(response.url)
        marca  = response.url.split("/")[2]
        print(marca)
        if marca == "www.maskota.com.mx":
            print("entre a mascota")
            quote = response.css('div.detallesProducto')[0]
            lista = quote.css('div.precio')
            precio = lista.css('strong.skuBestPrice::text').extract_first()
            print(precio);
        else:
            print("entre a petco: " + marca)
            precio = response.css(".variant_price span::text").extract_first() 
            print(precio)


#class QuotesSpider(scrapy.Spider):
    #name = "lol"
    #start_urls = [
    #    'https://www.petco.com.mx/petco/en/MARCAS/Royal-Canin/Royal-Canin-Labrador-Para-Cachorro/p/BP_104859',
    #    ]
    #def parse(self, response):
        #quote = response.css('div.span-11 productDescription last')[0]
        #lista = quote.css('div.variants')
        #precio = lista.css('span.price::text').extract_first()
        #print(precio)
        
        #print(quote.css("span.text::text").extract_first)
        
        # for quote in response.css('div.quote'):
        #     yield {
        #         'text': quote.css('span.text::text').extract_first(),
        #         'author': quote.css('span small::text').extract_first(),
        #         'tags': quote.css('div.tags a.tag::text').extract(),
        #         }