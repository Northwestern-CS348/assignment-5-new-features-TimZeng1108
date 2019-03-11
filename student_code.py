import languageTools, utilities, reader, kb, memory, core

#Red = "\u001b[31m"
#Grn = "\u001b[32m"
#Ylw = "\u001b[33m"
#Blu = "\u001b[34m"
#Mag = "\u001b[35m"
#Cyn = "\u001b[36m"
#
#rd = "\033[31;1m"
#em = "\033[4m"
#st = "\033[0m"

Red = ""
Grn = ""
Ylw = ""
Blu = ""
Mag = ""
Cyn = ""

rd = ""
em = ""
st = ""
lf = "\n"


def buildFeatureStatement(tree):

    print("Stubbed out version of buildFeatureStatement")

    root = languageTools.extractRoot(tree)
    subject = languageTools.extractSubject(root)

    namelist = core.resolveObjectFOPC(subject)

    core.findAndAttachPrepObjectsFOPC(root, subject, namelist)

    core.findAndAssertFeaturesFOPC(root, namelist)
    core.findAndAssertDefinitionsFOPC(root, namelist)
