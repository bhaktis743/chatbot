import random
import datetime


def greet():
    responses = ["Welcome to RISE UNIVERSITY , I am admission enquiry chatbot SHIKSHA. How can I help you today?"]
    return random.choice(responses)

def select():
    responses = ['I can help you with the queries realated to 1]college information , 2]streams , 3]admission process , 4]contact, 5]address for more help visit our website www.riseuni.in']
    return random.choice(responses)
    
def college_info():
    responses = ['We offer a wide range of majors, including Business, Engineering, and Liberal Arts.'
                'Our tuition rates are competitive with other colleges in the area.',
                'Our college provides excellent academic programs in fields like Business, Computer Science, Engineering, and more.'
                'Our tuition rates are very affordable.',
                'At our college, we have a  variety of programs to choose from, including Business, Liberal Arts, and Health Sciences.'
                ' Our tuition rates are very reasonable.']
    return random.choice(responses)

def streams ():
    responses = ["We offer various streams like Engineering, science, Arts and Commerce.", 
    "We have streams such as Engineering, Science, Arts and Commerce.", 
    "Our college provides streams like Engineering, Science, Arts and Commerce."]
    return random.choice(responses)

def Engineering():
    responses = ["We offer various streams like Computer Science and Engineering ,Electronics and Communication Engineering,Mechanical Engineering ,Civil Engineering ,Chemical Engineering",
    "We have various streams like Computer Science and Engineering ,Electronics and Communication Engineering,Mechanical Engineering ,Civil Engineering ,Chemical Engineering",
    "Our college provides streams like Computer Science and Engineering ,Electronics and Communication Engineering,Mechanical Engineering ,Civil Engineering ,Chemical Engineering"]
    return random.choice(responses)

def Science():
    responses =["We offer various courses like Physics ,Chemistry ,Biology , Mathematics, Computer Science",
    "We have different streams in science like Physics ,Chemistry ,Biology , Mathematics, Computer Science",
    "Our college provides streams in science like Physics ,Chemistry ,Biology , Mathematics, Computer Science"]
    return random.choice(responses)

def Arts():
    responses = ["We have various arts courses such as Literature, History, Sociology, Psychology and Political Science.",
     "We have arts courses like Literature, History, Sociology, Psychology and Political Science.", 
     "Our college provides arts courses such as Literature, History, Sociology, Psychology and Political Science.",    
    ]
    return random.choice(responses)

def Commerse():
    responses =[
        "We offer various commerce courses such as Accounting, Finance, Marketing, Business Management and Economics.",
         "We have commerce courses like Accounting, Finance, Marketing, Business Management and Economics.", 
         "Our college provides commerce courses such as Accounting, Finance, Marketing, Business Management and Economics."
    ]
    return random.choice(responses)

def contact ():
    responses = [
        "You can reach us at our phone number 1234567890 or email us at riseuni@gmail.com.",
         "If you have any further questions, please contact us at 1234567890 or email us at riseuni@gmail.com.", 
        "For any queries, you can get in touch with us at our phone number 1234567890 or email us at riseuni@gmail.com."
    ]
    return random.choice(responses)

def admission():
    responses =[
        'Our admission process involves submitting an online application and providing transcripts, test scores, and letters of recommendation. We also require a personal essay and an admissions interview for some programs.', 
        "To apply to our college, you'll need to complete an online application and provide transcripts, test scores, and letters of recommendation. Some programs also require a personal essay and an admissions interview.", 
        "Our admission process is straightforward. You'll need to complete an online application and provide transcripts, test scores, and letters of recommendation. Some programs also require a personal essay and an admissions interview."
    ]
    return random.choice(responses)

def address():
    responses = [
        'Our college is located at 456 Main Street, Anytown INDIA. We have plenty of parking and are easily accessible by public transportation. ',
        'Our campus is located at 456 mainStreet, Anytown INDIA. We have a beautiful campus with lots of green space and modern facilities.', 
        'You can find us at 456 main Street, Anytown INDIA. Our campus is conveniently located near downtown and the city cultural district.']
    return random.choice(responses)

def goodbye():
    responses = ['Good bye! Have a great day.', 'Thank you for your interest in our college. Have a nice day!', 'Bye! It was nice talking to you.']
    return random.choice(responses)