from pyscript import display, document


def general_weighted_average(e):
    document.getElementById('stdnt_info').innerHTML = ' '
    document.getElementById('smmry').innerHTML = ' '
    document.getElementById('output').innerHTML = ' '
    subjects = ['bchem', 'fashion', 'math', 'engfiljp', 'tech', 'pe']
    units_subject = (5, 3, 2, 1)

    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    bchem = float(document.getElementById('bchem').value)
    fashion = float(document.getElementById('fashion').value)
    math = float(document.getElementById('math').value)
    engfiljp = float(document.getElementById('engfiljp').value)
    tech = float(document.getElementById('tech').value)
    pe = float(document.getElementById('pe').value)

    weighted_sum = (bchem * units_subject[0] + 
           math * units_subject[0] + 
           fashion * units_subject[0] + 
           engfiljp * units_subject[1] + 
           tech * units_subject[2] + 
           pe * units_subject[3]) 
    total_units = (units_subject[0] * 3) + units_subject[1] + units_subject[2] + units_subject[3]
    gwa = weighted_sum / total_units
    
    summary = f"""{subjects[0]}: {bchem:.0f}
{subjects[1]}: {fashion:.0f}
{subjects[2]}: {math:.0f}
{subjects[3]}: {engfiljp:.0f}
{subjects[4]}: {tech:.0f}
{subjects[5]}: {pe:.0f}
    """
    display(f'Name?!: {first_name} {last_name}', target="stdnt_info")
    display(summary, target='smmry')
    display(f'Your GWA is {gwa:.2f} ╮( ˘ ､ ˘ )╭', target='output', )