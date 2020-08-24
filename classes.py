class point:
  def __init__(self,x,y,z):
    self.x=x
    self.y=y
    self.z=z

class item:
  def __init__(self,mpoint,name):
    self.mpoint=mpoint
    self.name=name
  def dist_from_main(self,main_item):
    return ((self.mpoint.x-main_item.x)**2+(self.mpoint.y-main_item.y)**2+(self.mpoint.z-main_item.z)**2)**0.5