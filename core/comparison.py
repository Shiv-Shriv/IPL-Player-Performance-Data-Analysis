GREEN = "#22C55E" 
RED = "#EF4444"
WHITE = "#FFFFFF"

def higherstatcmp(valuetodisplay, valuetocompare):
    if(valuetodisplay>valuetocompare):
        return "GREEN"
    elif(valuetodisplay==valuetocompare):
        return "WHITE"
    else:
        return "RED"
    
def lowerstatcmp(valuetodisplay, valuetocompare):
    if(valuetodisplay<valuetocompare):
        return "GREEN"
    elif(valuetodisplay==valuetocompare):
        return "WHITE"
    else:
        return "RED"
    
def statcolor(label, value, color):
    return f"""
    <div style="margin-bottom:1rem;">
        <div style="font-size:0.875rem;">
            {label}
        </div>
        <div style="font-size:2.25rem; font-weight:600; color:{color}; line-height:1.2;">
            {value}
        </div>
    </div>
    """