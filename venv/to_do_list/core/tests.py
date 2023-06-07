from django.test import TestCase
from .models import AtividadeModel


class IndexTest(TestCase):   
    def setUp(self): 
        self.resp = self.client.get('/')    
    
    def test_sucesso(self): 
        self.assertEqual(200, self.resp.status_code)

    def test_conteudo(self):
        self.assertContains(self.resp, 'hoje')
        
    def test_template(self):
        self.assertTemplateUsed(self.resp, 'index.html')


class CadastroTest(TestCase):
    def setUp(self):
        self.resp = self.client.get('/cadastro')
    
    
    def test_sucesso(self):     
        self.assertEqual(301, self.resp.status_code)
    
    
    def test_template(self):
        self.assertTemplateUsed('cadastro.html')

class AtividadeModel(TestCase):
    
    def setUp(self):
        
        
        def setUp(self):
            self.item = AtividadeModel(
                nome = 'atividade',
                tipo = 'tipo',
                descricao = 'descricao da atividade',
                data = '2023-05-07'
            )            
            self.item.save()      

        #Testar se existem objetos criados 
        def test_objetoExiste(self):  
            self.assertTrue( AtividadeModel.objects.exists())
            
        #Verificar se foi criado apenas um registro
        def test_qtdObjetos(self):
            self.AssertTrue( len (AtividadeModel.objects.all()) == 1)
