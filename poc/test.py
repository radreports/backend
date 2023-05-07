import redis

red = redis.StrictRedis('localhost',6379,password="m0bdat")
res = {
    "Task":"liver"
}
red.publish("test","test")
