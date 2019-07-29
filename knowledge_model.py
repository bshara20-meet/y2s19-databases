from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class Wiki(Base):
	# Create a table with 4 columns


   __tablename__ = 'i'
   art_num = Column(Integer, primary_key=True)
   name = Column(String)
   topic = Column(String)
   rate = Column(Integer)
   def __repr__(self):
         return (" Name: {}\n"
                 "topic: {} \n"
                 "rating: {}").format(
                      self.name, self.topic, self.rate)

x=Wiki(name="discover the nature",topic="duck",rate=4)
print(x)
# The first column will be the primary key
# The second column should be a string representing
# the name of the Wiki article that you're referencing
# The third column will be a string representing the 
# topic of the article. The last column will be
# an integer, representing your rating of the article.

pass