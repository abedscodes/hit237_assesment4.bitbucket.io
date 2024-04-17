from django.shortcuts import render

# Create your views here.

def about(request):
    context={
        'admin_list': create_admins(),
    }
    return render(request, 'proj_app/about.html', context)

def home(request):
    context = {}
    return render(request, 'proj_app/home.html', context)

def proj_list(request):
    context={
        'proj_list': create_topics(),
    }
    return render(request, 'proj_app/project_list.html', context)

def project_details(request, topic_id):
    # Retrieve the project with the given ID
    projects = create_topics()
    project = None
    for proj in projects:
        if proj.id == topic_id:
            project = proj
            break

    context = {
        'project': project
    }
    return render(request, 'proj_app/project_details.html', context)

def create_admins():
    admin_list=[]

    admin_list.append(Admin(361066,
                            'Moiz Ali'))
    admin_list.append(Admin(361222,
                            'Muhammed Abed'))
    admin_list.append(Admin(365145,
                            'Heshara Danathma Balasooriya Balasooriya Mudiyanselage'))
    admin_list.append(Admin(365635,
                            'Gokul Ashok'))      
    return admin_list


# Define Admin class
class Admin:
    def __init__(self, id, name):
        self.id = id
        self.name= name

    
    def __str__(self):
        return str(self.id) +", " + self.name


# Define Topic Class
class Topic():
    def __init__(self, id, title, catg, description, brief_description, supervisor, cas, syd, ext, chem, civil,
                 eee, mech, cs, cyber, datasc, infosys, seng):
        self.id = id
        self.title = title
        self.catg = catg
        self.description = description
        self.brief_description = brief_description
        self.supervisor = supervisor
        self.cas = cas
        self.syd = syd
        self.ext = ext
        self.chem = chem
        self.civil = civil
        self.eee = eee
        self.mech = mech
        self.cs = cs
        self.cyber = cyber
        self.datasc = datasc
        self.infosys = infosys
        self.seng = seng

        def __str__(self):
            return self.title
      
def create_topics():
    topic_list=[]

    topic_list.append(Topic(1,
                            'Machine learning approaches for Cyber Security ',
                            'Artificial Intelligence, Machine Learning and Data Science',
                            'As we use internet more, the data produced by us is enormous. But are these data being secure? The goal of applying machine learning or intelligence is to better risk modelling and prediction and for an informed decision support. Students will be working with either supervised or unsupervised machine learning approaches to solve the problem/s in the broader areas of Cyber Security.',
                            'Internet usage generates vast amounts of data, raising security concerns. Machine learning aims to enhance risk modeling and prediction for informed decision-making in cybersecurity, employing supervised or unsupervised methods for student projects.',
                            'Bharanidharan Shanmugam',
                            True,
                            True,
                            True,
                            False,
                            False,
                            False,
                            False,
                            True,
                            False,
                            False,
                            True,
                            True))
    topic_list.append(Topic(9,
                            'Informetrics applications in multidisciplinary domain',
                            'Artificial Intelligence, Machine Learning and Data Science',
                            'Informetrics studies are concerned with the quantitative aspects of information. The applications of advanced machine learning, information retrieval, network science and bibliometric techniques on various information artefact have contributed fresh insights into the evolutionary nature of research fields. This project aims at discovering informetric properties of multidisciplinary research literature using various machine learning, network analysis, data visualisation and data wrangling tools.',
                            'Informetrics explores quantitative aspects of information. Combining advanced machine learning, information retrieval, and network science, this project delves into multidisciplinary research literature to uncover informetric properties using data analysis and visualization tools.',
                            'Yakub Sebastian',
                            True,
                            True,
                            True,
                            False,
                            False,
                            False,
                            False,
                            True,
                            True,
                            True,
                            True,
                            True))
    topic_list.append(Topic(16,
                            'Development of a Virtual Reality System to Test Binaural Hearing',
                            'Biomedical Engineering and Health Informatics',
                            'A virtual reality system could be used to objectively test the binaural hearing ability of humans (the ability to hear stereo and locate the direction and distance of sound). This project aims to design, implement and evaluate a VR system using standard off the shelf components (VR goggle and headphones) and standard programming techniques.',
                            'This project develops a VR system to objectively test human binaural hearing abilities, enabling sound localization assessments using standard VR components and programming methods.',
                            'Sami Azam',
                            True,
                            False,
                            True,
                            False,
                            False,
                            True,
                            False,
                            True,
                            False,
                            False,
                            False,
                            True))
    topic_list.append(Topic(41,
                            'Current trends on cryptomining and its potential impact on cryptocurrencies',
                            'Cyber Security',
                            """Cryptomining is the process of mining crypto currencies by running a sequence of algorithms. Traditionally, to mine new crypto coins, a person (or group of people) would buy expensive computers and spend a lot of time and money running them to perform the difficult calculations to generate crypto coins. Some website owners have started taking a different approach; they have put the software which runs those difficult calculations into their website's Javascript. This then causes the computers belonging to the visitors of their website to run those calculations for them, instead of running them themselves. In other words, when you visit a website with an embedded crypto-miner in it, your computer and electricity is used to try to generate crypto-coins for the owners of that website. Although there are various measures being applied to stop these illegitimate minings, the trend is still increasing. This research aims to find out potential gaps in current methodologies and develop a solution that can fulfil the gap. It also aims to find out:
                            •	What type crypto mining methodologies are being applied?
                            •	Apart from crypto-mining, what other security risks may it introduce? For example: cryptojacking
                            •	How current web standards are tackling this problem?""",
                            "Cryptomining involves running algorithms to mine cryptocurrencies. Some websites embed crypto-mining scripts in their JavaScript, exploiting visitors' CPUs. This research seeks to address gaps in current methodologies and explore associated security risks like cryptojacking.",
                            'Sami Azam',
                            True,
                            True,
                            True,
                            False,
                            False,
                            False,
                            False,
                            True,
                            True,
                            False,
                            False,
                            True))
    
    topic_list.append(Topic(176,
                            'Artificial Intelligence in Health Informatics',
                            'Artificial Intelligence, Machine Learning and Data Science',
                            'The project aims to use multiple publicly available health datasets to formulate a different dataset that may have features from the original set along with new ones developed through feature engineering. The dataset will then be used to build predictive model based on both general and deep learning based algorithm. The findings will be analysed and compared to similar research works.',
                            'This project aims to merge public health datasets, enhancing them through feature engineering. A predictive model will be developed using both traditional and deep learning algorithms, with results analyzed and compared to existing research.',
                            'Asif Karim',
                            True,
                            True,
                            True,
                            False,
                            False,
                            True,
                            False,
                            True,
                            False,
                            True,
                            False,
                            True))
    
    topic_list.append(Topic(180,
                            'Unsupervised Model Development from Autism Screening Data ',
                            'Artificial Intelligence, Machine Learning and Data Science',
                            'The proposed system will present a two-cluster solution from a given dataset which will group toddlers based on multiple common medical traits. In depth literature survey of similar studies, both supervised and unsupervised will be carried out before the cluster-based model is implemented. The solution will be validated using both External and Internal validation measures and statistical significance tests.',
                            'This system will cluster toddlers based on medical traits from a dataset. A comprehensive literature review on similar studies will precede the implementation of a cluster-based model. Validation will utilize external/internal measures and statistical tests.',
                            'Asif Karim',
                            True,
                            True,
                            True,
                            False,
                            False,
                            True,
                            False,
                            True,
                            False,
                            True,
                            False,
                            True))
    
    topic_list.append(Topic(226,
                            'Applying Artificial Intelligence to solve real world problems ',
                            'Artificial Intelligence, Machine Learning and Data Science',
                            'Artificial Intelligence has been used in many applications to solve certain problems through out the academia and the industry – from electricity to writing text. AI has a multitude of applications and this project will pick up a problem and explore the applications of AI with minimal human intervention. Examples of applications include -building a bot, predicting the power usage, spam filtering and the list is endless.',
                            'AI is widely applied across academia and industry, tackling diverse challenges from electricity to text generation. This project selects a specific problem and investigates AI applications with minimal human involvement, such as building bots, power usage prediction, and spam filtering.',
                            'Bharanidharan Shanmugam',
                            True,
                            True,
                            True,
                            True,
                            True,
                            True,
                            True,
                            True,
                            True,
                            True,
                            True,
                            True))
    print (topic_list)
      
    return topic_list