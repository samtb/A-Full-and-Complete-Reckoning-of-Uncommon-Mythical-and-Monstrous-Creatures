#!/usr/bin/python
# helpful animal list found here: https://github.com/hzlzh/Domain-Name-List/blob/master/Animal-words.txt
import random
import argparse


parser = argparse.ArgumentParser(description='Hybrid animal encyclopedia generator')
parser.add_argument('soManyAnimals', type=int, help='how many animals do you want to create?')
args = parser.parse_args()

animalList = ['aardvark','albatross','alligator','alpaca','ant','anteater','antelope','ape','armadillo','ass','donkey','baboon','badger','barracuda','bat','bear','beaver','bee','bison','boar','buffalo','butterfly','camel','caribou','cat','caterpillar','cattle','cheetah','chicken','chimpanzee','chinchilla','clam','cobra','cockroach','cod','cormorant','coyote','crab','crane','crocodile','crow','deer','dinosaur','dog','dogfish','dolphin','donkey','dove','dragonfly','duck','eagle','eel','elephant','elephant seal','elk','emu','falcon','ferret','finch','fish','flamingo','fly','fox','frog','gazelle','gerbil','giant panda','giraffe','gnat','gnu','goat','goose','goldfinch','goldfish','gorilla','grasshopper','grouse','guinea fowl','guinea pig','gull','hamster','hare','hawk','hedgehog','heron','herring','hippopotamus','hornet','horse','human','hummingbird','hyena','jackal','jaguar','jay','jay, blue','jellyfish','kangaroo','koala','komodo dragon','kudu','lark','lemur','leopard','lion','llama','lobster','locust','loris','louse','lyrebird','magpie','mallard','manatee','marten','meerkat','mink','mole','monkey','moose','mouse','mosquito','mule','narwhal','newt','nightingale','octopus','okapi','opossum','oryx','ostrich','otter','owl','ox','oyster','panther','parrot','partridge','peafowl','pelican','penguin','pheasant','pig','pigeon','pony','porcupine','porpoise','prairie dog','quail','rabbit','raccoon','ram','rat','raven','red deer','red panda','reindeer','rhinoceros','rook','salamander','salmon','sand dollar','sandpiper','sardine','scorpion','sea lion','sea urchin','seahorse','seal','shark','sheep','shrew','shrimp','skunk','slow loris','snail','snake','spider','squid','squirrel','starling','stingray','stinkbug','stork','swallow','swan','tapir','termite','tiger','toad','trout','turkey','turtle','viper','vulture','wallaby','walrus','wasp','water buffalo','weasel','whale','wolf','wolverine','wombat','woodcock','woodpecker','worm','wren','yak','zebra']
habitatList = ['humid','cold','damp','freezing','murky','windblown','fluorescent','grim','gross but not altogether repulsive','salty','sour smelling','tepid','lime scented','vast and favorable','whimsical','stinky','dank']
habitatLocationList = ['holes in the ground','seashores','underwater bunkers','exotic dungeons','bogs','trundle beds','moss patties','shampoo bottles and other human detritus','creeks','riverbeds','rivers','oceans','underground dwellings','crypts']
consumeList = ['eats','sustains itself on the shed skin of local groups of','regularly feeds on','enjoys killing and eating large numbers of','can swallow a whole','finds solace in the den of the','likes to carouse with groups of animals closely related to the','lives on the waste of the','is a parasite of the','can live for years on the dandruff shed by a single','is a fantastic mimic of the mighty','can make a sound like a','can be far more intimidating than an elder']
sizeList = ['about three times shorter but five times as wide as a mature','often found to grow taller than the height of six full grown','sometimes found towering over even the tallest','smaller than a typical','more massive than five','similar in size to the','bigger than your average','much smaller than an average','fifty times larger than the standard','is not quite as big as a baby','is thinner but bulkier than a couple of','is rounder but not quite as cute as an adolescent','is over all squishier than the male']
originList = ['a hybrid of the','a mashup between the','the result of repeated romantic encounters between the','the result of an odd pairing between the','a marriage between the']
canBeFoundInList = ['can be found around','is likely to be found alongside','is known to frequent','will find a home in and around','is capable of spending its entire life by','can only survive in the proximity of','will only thrive in','lives by','breeds in']
soManyAnimals = args.soManyAnimals

def adverbDegree():
    return (random.choice(adverbDegreeList))

def org():
    return (random.choice(orgList))

def thing():
    return (random.choice(thingList))

def canBeFoundIn():
    return (random.choice(canBeFoundInList))

def origin():
    return (random.choice(originList))

def size():
    return (random.choice(sizeList))

def animal():
    return (random.choice(animalList))

def consume():
    return (random.choice(consumeList))

def habitat():
    return (random.choice(habitatList))

def habitatLocation():
    return (random.choice(habitatLocationList))

def prefix():
    sourceAnimal = (random.choice(animalList))
    x = len(sourceAnimal)
    pre = sourceAnimal[:x/2]
    if x > 3:
        return [sourceAnimal,x,pre]
    else:
        return [sourceAnimal,x,sourceAnimal]
        
def suffix():
    sourceAnimal = (random.choice(animalList))
    x = len(sourceAnimal)
    suf = sourceAnimal[-x/2:]
    if x > 3:
        return [sourceAnimal,x,suf]
    else:
        return [sourceAnimal,x,sourceAnimal]

def newAnimalData():
    animal1 = prefix()
    animal2 = suffix()
    f = prefix()[2]+suffix()[2]
    newAnimalName = animal1[2]+animal2[2]
    newAnimalDescription = origin(),animal1[0],'and the',animal2[0]+'. '
    extendedDescription = 'The',newAnimalName,'is',size(),animal()+'. It',consume(),animal(),'and',canBeFoundIn(),habitat(),habitatLocation()+'. '
    return [newAnimalName,newAnimalDescription,extendedDescription]

def createAnimalList(x):
    count = 0
    animalList = []
    while count < x:
        newA = newAnimalData()
        animal1 = newA[0].upper()
        animal2 = ' '.join(newA[1]).capitalize()
        animal3 = ' '.join(newA[2])
        theAnimalInfo = '\nAnimal: %s \nOrigin: %s \nDescription: %s'% (animal1,animal2,animal3)
        animalList.append(theAnimalInfo)
        count = count + 1
    return (animalList)

def makeTitle():
    title = 'An Encyclopedia of',adverbDegree().capitalize(),org().capitalize(),thing().capitalize()
    return ' '.join(title)

# Main funciton
def main():
    print 'A Full and Complete Reckoning of Uncommon, Mythical, and Monstrous Creatures'
    print '\n'.join(sorted(createAnimalList(soManyAnimals)))



# EXECUTE
main()
