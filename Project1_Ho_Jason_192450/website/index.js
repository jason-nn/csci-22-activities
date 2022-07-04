const foodLabels = Array.from(document.querySelectorAll('label')).filter(
  (node) => node.textContent.startsWith('Food')
);
let foodItems = foodLabels.length / 2;
const addFoodButton = document.querySelector('#add-food-button');
const box = document.querySelector('.box');

addFoodButton.addEventListener('click', () => {
  const foodDiv = document.createElement('div');

  const foodLabel = document.createElement('label');
  foodLabel.textContent = `Food ${foodItems + 1}`;
  foodLabel.htmlFor = `food-${foodItems + 1}`;
  foodDiv.append(foodLabel);

  const foodSelect = document.createElement('select');
  foodSelect.name = `food-${foodItems + 1}`;
  foodSelect.id = `food-${foodItems + 1}`;
  const optionOne = document.createElement('option');
  const optionTwo = document.createElement('option');
  const optionThree = document.createElement('option');
  optionOne.value = 'chicken-curry';
  optionOne.textContent = 'Chicken Curry';
  optionTwo.value = 'beef-curry';
  optionTwo.textContent = 'Beef Curry';
  optionThree.value = 'tonkatsu-curry';
  optionThree.textContent = 'Tonkatsu Curry';
  foodSelect.append(optionOne, optionTwo, optionThree);
  foodDiv.append(foodSelect);

  const quantityDiv = document.createElement('div');

  const quantityLabel = document.createElement('label');
  quantityLabel.textContent = `Food ${foodItems + 1} Quantity`;
  quantityLabel.htmlFor = `food-${foodItems + 1}-quantity`;
  quantityDiv.append(quantityLabel);

  const quantityInput = document.createElement('input');
  quantityInput.type = 'number';
  quantityInput.id = `food-${foodItems + 1}-quantity`;
  quantityDiv.appendChild(quantityInput);

  foodItems += 1;

  box.insertBefore(foodDiv, addFoodButton.parentNode);
  box.insertBefore(quantityDiv, addFoodButton.parentNode);
});
