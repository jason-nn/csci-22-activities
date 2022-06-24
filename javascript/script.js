const myList = document.getElementById('my-list');
const allParagraphs = document.getElementsByTagName('p');

const groupOne = document.getElementById('group1');
const groupOneParagraphs = groupOne.getElementsByTagName('p');

const mainTitle = document.getElementById('main-title');
mainTitle.textContent = 'My JavaScript Page';

const mySection = document.getElementById('my-section');
const mySectionHeading = document.createElement('h2');
mySectionHeading.textContent = 'My Section Heading';
mySection.appendChild(mySectionHeading);

for (let i = 0; i < 3; i++) {
  const item = document.createElement('p');
  item.textContent = `Item ${i + 1}`;
  mySection.appendChild(item);
}

const listItem = document.createElement('li');
listItem.textContent = 'List Item 1';

const listItemTwo = document.createElement('li');
listItemTwo.textContent = 'List Item 2';

mySection.append(listItem, listItemTwo);
