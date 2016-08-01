Router.configure({
    // tell iron router to render our individual templates inside of our masterLayout template
    layoutTemplate: "masterLayout"
});

Router.route('/', {// describe the route path, '/' - root path of our web app
    name: 'topChart',// the template this route will use
    waitOn: function() {
      // iron router will hold off rendering our page until the waitOn function completes
      // returns a subscription to our “apps” publication
      // passes	a	set	of options to	the	server,
      // tells	the	server	to	sort	our	apps	based	off	of	avgRating and	app_id.	And	to only	give us	a	max	of	20	results.
        Meteor.subscribe('apps', {sort: {avgRating: -1, app_id: -1}, limit: 50});
    },
    // The return	value	of the data function becomes the Blaze template’s	“data	context”.
    // returns an	object with	a	single property	“apps” that	contains all the Apps returned via	our	subscription.
    data: function () {
        return {
            apps: Apps.find({}, {sort: {avgRating: -1, app_id: -1}, limit: 50})
        };
    }
});


Router.route('/app/:_id', {//’:’ tells Iron	Router that this is a variable that will be bound to the _id parameter
    name: 'appPage',
    waitOn: function() {
      // pass the app id passed in the url by using this.params._id
        Meteor.subscribe('singleApp', this.params._id);
    },
    data: function () {
      // bind the app with the given id to the data context of template
        return Apps.findOne(this.params._id);
    }
});
