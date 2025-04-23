# app/routes.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
import csv
from datetime import datetime

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return render_template('index.html')

@main.route('/add', methods=['GET', 'POST'])
def add_expense():
    if request.method == 'POST':
        date = request.form['date']
        category = request.form['category']
        amount = request.form['amount']

        # Save to a CSV file
        with open('expenses.csv', mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([date, category, amount])

        flash('Expense added successfully!', 'success')
        return redirect(url_for('main.view_expenses'))

    return render_template('add.html')

@main.route('/view')
def view_expenses():
    expenses = []
    try:
        with open('expenses.csv', mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) == 3:
                    expenses.append({'date': row[0], 'category': row[1], 'amount': row[2]})
    except FileNotFoundError:
        pass  # No expenses yet

    return render_template('view.html', expenses=expenses)

@main.route('/about')
def about():
    return render_template('about.html')