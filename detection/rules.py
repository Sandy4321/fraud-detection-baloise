#import data
# return tuple (int, String)
class RuleDetection:
    def isFraud(self, damage):
        
        # Hagel Regel
        if damage.data['VERSARTGRP'] == 'MF Kasko' &&
           damage.data['VERSART'] == 'Teilkasko' &&
           damage.data['SDART'] == 'Elementar' &&
           damage.data['SDURS'] == 'Hagel':
            # TODO: if hagel return true, else false
            # damage.data['SDERDAT']
        
        # Iphone
        if damage.data['VERSARTGRP'] == 'Wertsachen' &&
           damage.data['VERSART'] == 'einfacher Diebstahl' &&
           damage.data['SDART'] == 'Kombiversicherung Privathaushalt' &&
           damage.data['SDURS'] == 'einfacher Diebstahl' &&:
        
            
        
