from model.contact_modification import Contact_modification

def test_contact_modification(app):
    app.contacts.contact_modify(Contact_modification("NuPavel", "neznayu", "NuTsios", "Nuraynalds", "NuQA", "Nudevhouse", "Kavkaz", "1111111", "utreoos@devhouese.pro"))
