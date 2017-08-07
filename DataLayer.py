from threading import Thread
import GlobalFunctions as gf
import GlobalVariables as gv
import Config          as cf
from TagPallete import TagElementFactory, TagElementConfig
from TagPallete import LoadTagElement 

''' ############ Legend #############

method names lower case seperated by underscore per PEP 8
https://www.python.org/dev/peps/pep-0008/

************************
han moniker is short for handle.
Raymond S.
'''

class MainObjectDataHandler(Thread):
    
    def __init__(self, parent):
        
        self.parent        = parent
        self.tagName       = None
        self.tagDataSet    = None
        self.GPIO          = None
        
        self.activeObjects = []
        self.han_database()
        
    def han_data_harmony(self, instruction, tagName=None):
        self.han_stop_thread_link()
        
        self.instruction = instruction
        if instruction == 'add':
            self.tagName = self.han_create_tag_name()
        else:  
            self.tagName = tagName
    
        for obj in self.activeObjects:
            obj.han_task_route(instruction)
       
        self.db.han_db_obj_sync()  
        
        self.han_load_gpio_element()
        self.han_start_thread_link()
        
    def han_load_gpio_element(self):
        try:
            self.parent.scan.han_load_GPIO_btn()
        except:
            pass
    def han_stop_thread_link(self):
        try:
            self.parent.scan.han_stop_tag_scan()
        except:
            pass
    def han_start_thread_link(self):
        try:
            self.parent.scan.han_start_tag_scan()
        except:
            pass

    def han_obj_data_init(self): 
        db = gv.tagElements
        for i in db:
            self.tagName    = i      
            self.tagCanvasDH.han_item_load(self.tagName)
            self.treeViewDH.han_item_add()
           
    def han_treeview_data(self, treeviewClassInst):
        self.treeClass       = treeviewClassInst
        self.treeViewObj     = self.treeClass.treeViewObj
        self.treeViewDH      = TreeViewDataHandler(self)
        self.activeObjects.append(self.treeViewDH)
          
    def han_tagcanvas_data(self, tagPalleteClassInst):
        self.tagPalleteClass = tagPalleteClassInst
        self.tagCanvasObj    = self.tagPalleteClass.canvasObj
        self.tagCanvasDH     = TagDataHandler(self)
        self.activeObjects.append(self.tagCanvasDH)
        
    def han_gpio_data(self):
        self.gpioInit      = True

    def han_database(self):
        self.db = DataBaseDataHandler(self)
        self.activeObjects.append(self.db)
          
    def get_assigned_tags(self):
        taglist = []
        for i in self.tagCanvasObj.find_all():
            if len(self.tagCanvasObj.gettags(i))==0:
                continue
            tagName =  self.tagCanvasObj.gettags(i)[1]
            taglist.append(tagName)
        return taglist
    
    def han_create_tag_name(self):     
        canvasTagList = self.get_assigned_tags()
        self.num = gf.handleGetAvailableTagName(canvasTagList)
        return 'Tag-%s' % self.num
    
    def han_item_GPIO_bind(self, tagName, GPIOParent, GPIO, isGPIOBound):
        #self.han_stop_thread_link()
        self.tagname     = tagName
        self.GPIOParent  = GPIOParent
        self.GPIO        = GPIO
        self.isGPIOBound = isGPIOBound
        self.db.han_tag_gpio_bind()
        self.db.han_db_obj_sync()
        self.han_load_gpio_element()
        #self.han_start_thread_link()
    
    
##############################################################################
class TagDataHandler():
    
    def __init__(self, parent):
        self.parent          = parent
        self.tagPalleteClass = self.parent.tagPalleteClass
        self.canvas          = self.tagPalleteClass.canvasObj
        self.GPIO            = self.parent.GPIO
        self.routeDict     = {
                                 'add':self.han_item_add,
                              'remove':self.han_item_remove, 
                              'update':self.han_item_update,
                              'rename':self.han_item_rename
                              }
    def han_task_route(self, instruction):
        self.instruction = instruction
        self.tagName     = self.parent.tagName
        self.tagDataSet  = self.parent.tagDataSet
        self.task        = self.routeDict.get(self.instruction, None)
        if self.task != None:
            self.task()
        
    def han_item_add(self):
        TagElementFactory(self.tagPalleteClass, self.tagName)
        TagElementConfig(self.tagPalleteClass, self.tagName)
    
    def han_item_load(self, tagName):
        LoadTagElement(self.tagPalleteClass, tagName)
        TagElementConfig(self.tagPalleteClass, tagName)
        
    def han_item_remove(self):
        self.canvas.delete(self.tagName)
    
    def han_item_update(self):
        pass
    
    def han_item_rename(self):
        pass  
    
    def han_item_GPIO_bind(self):
        GPIO = 'GPIO%s' % self.GPIO
        self.canvas.addtag(GPIO, 'withtag', self.tagName)
              
##############################################################################             
class TreeViewDataHandler():
    
    def __init__(self, parent):
        self.parent = parent
        self.treeClass = parent.treeClass
        self.treeview = self.treeClass.treeViewObj
        
        self.routeDict     = {
                                 'add':self.han_item_add,
                              'remove':self.han_item_remove, 
                              'update':self.han_item_update,
                              'rename':self.han_item_rename
                              }
    
    def han_task_route(self, instruction):
        self.instruction = instruction
        self.tagName     = self.parent.tagName
        self.task        = self.routeDict.get(self.instruction, None)
        if self.task != None:
            self.task()
        
    def han_item_add(self):
        self.tagName     = self.parent.tagName
        self.treeview.insert('', 'end', text=self.tagName, 
                             value=(self.tagName))
              
    def han_item_remove(self):
        idx = self.get_tag_idx()
        self.treeview.delete(idx)
                
    def han_item_update(self):     
        pass
    
    def han_item_rename(self):
        pass  
        
    def get_tag_idx(self):       
        for idx in self.treeview.get_children():
            tagNameValue = self.treeview.item(idx)['values'][0]
            if tagNameValue == self.tagName:
                return idx 
              
##############################################################################
class DataBaseDataHandler():

        
    def __init__(self, parent):
        self.parent = parent   
        self.routeDict     = {
                                 'save':self.han_db_save,
                               'remove':self.han_item_remove, 
                                 'sync':self.han_db_obj_sync,
                              }
    def han_task_route(self, instruction):
        self.instruction = instruction
        self.tagName     = self.parent.tagName
        self.task        = self.routeDict.get(self.instruction, None)
        if self.task != None:
            self.task()
        
    def han_db_obj_sync(self):
        #gv.tagElements= {}
        self.canvas = self.parent.tagCanvasObj  
        for i in self.canvas.find_all():
            if len(self.canvas.gettags(i))==0:
               continue
            try:
                tagName =  self.canvas.gettags(i)[1]
            except:
                continue
            try:
                elementClass = gv.tagElements[tagName]
            except:
                pass
                
            x1, y1, x2, y2 = self.canvas.coords(tagName)
            w = x2-x1
            h = y2-y1
            elementClass.han_update_meta('x1',x1)
            elementClass.han_update_meta('y1',y1)
            elementClass.han_update_meta('x2',x2)
            elementClass.han_update_meta('y2',y2)
            elementClass.han_update_meta('w',w)
            elementClass.han_update_meta('h',h)
            
            gv.tagElements[tagName] = elementClass
    
    def han_tag_gpio_bind(self):
        print('bind Tag:',self.parent.tagName,'to',self.parent.GPIOParent,'on port',int(self.parent.GPIO))   
        elementClass = gv.tagElements[self.parent.tagName]
  
        elementClass.han_update_meta('GPIO', int(self.parent.GPIO))

        elementClass.han_update_meta('GPIOParent', self.parent.GPIOParent)

        elementClass.han_update_meta('isGPIOBound', self.parent.isGPIOBound)

    def han_db_save(self):
        self.han_db_obj_sync()
        cf.saveTagFile()

    def han_item_remove(self):
        gv.tagElements.pop(self.tagName, None)
##############################################################################


