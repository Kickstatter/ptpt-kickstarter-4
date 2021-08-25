from flask import Flask, render_template, request

app = Flask(__name__)
categoryList = []
countryList = []

class parameters:
    def __init__(self, category, goal, campaign_start, campaign_end, country, initial_contr):
        """

        :param category:
        :param goal:
        :param campaign_start:
        :param campaign_end:
        :param country:
        :param initial_contr:
        """
        self.category = category
        self.goal = goal
        self.campaign_start = campaign_start
        self.campaign_end = campaign_end
        self.country = country
        self.initial_contr = initial_contr
        assert category in categoryList
        assert type(self.goal) == int
        # assert type(campaign_start) == datetime find a way to make these two parameters datetime objects
        # assert type(campaign_end) == datetime
        assert country in countryList
        assert type(self.initial_contr) == int

@app.route('/')
def form():
    return render_template('form.html')


@app.route('/data/', methods=['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"Wrong URL"
    if request.method == 'POST':
        form_data = request.form
        return render_template('data.html', form_data=form_data)


app.run()
