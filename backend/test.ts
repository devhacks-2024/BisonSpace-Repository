// import Course from "./models/courses";
// import User from "./models/users";

// const courses = [
//   {
//     name: {
//       officialName: "Introductory Programming: Think Like a Computer  3 cr  ",
//       shortName: "COMP 1000",
//       description:
//         "In this course students will learn to mentally simulate how a computer operates and read and write simple computer programs. ",
//     },
//   },
//   {
//     name: {
//       officialName:
//         "Introduction to Tools and Techniques in Computer Science 1  1.5 cr  ",
//       shortName: "COMP 1002",
//       description:
//         "This is a lab-based course. Every computer scientist needs to make use of an expansive set of modern computing tools and techniques",
//     },
//   },
//   {
//     name: {
//       officialName: "Introductory Computer Science 1  3 cr  ",
//       shortName: "COMP 1010",
//       description:
//         "An introduction to computer programming using a procedural high level language",
//     },
//   },
//   {
//     name: {
//       officialName: "Computer Programming for Scientists and Engineers  3 cr",
//       shortName: "COMP 1012",
//       description:
//         "In this course students will learn to mentally simulate how a computer operates and read and write simple computer programs. ",
//     },
//   },
//   {
//     name: {
//       officialName: "Introductory Computer Science 2  3 cr  ",
//       shortName: "COMP 1020",
//       description:
//         "More features of a procedural language, elements of programming. May not be held with COMP 1021",
//     },
//   },
//   {
//     name: {
//       officialName: "Computing: Ideas and Innovation  3 cr  ",
//       shortName: "COMP 1500",
//       description:
//         "An introduction to the topics of Computer Science and problem solving",
//     },
//   },
//   {
//     name: {
//       officialName: "Navigating Your Digital World  3 cr  ",
//       shortName: "COMP 1600",
//       description:
//         "Topics related to digital society such as security, encryption and data storage, issues of social and ethical importance, and current events ",
//     },
//   },
//   {
//     name: {
//       officialName: "Tools and Techniques in Computer Science 1  1.5 cr   ",
//       shortName: "COMP 2002",
//       description:
//         "This is a lab-based course. Every computer scientist needs to make use of an expansive set of modern computing tools and techniques",
//     },
//   },
//   {
//     name: {
//       officialName: "ools and Techniques in Computer Science 2  1.5 cr  ",
//       shortName: "COMP 2006",
//       description:
//         "An introduction to computer programming using a procedural high level language",
//     },
//   },
//   {
//     name: {
//       officialName: "COMP 2060  Special Topics in Computer Science  3 cr  ",
//       shortName: "COMP 2060",
//       description:
//         "In this course students will pursue a specific introductory topic, which will vary from year to year. This course can be completed as a topics course multiple times under different titles. ",
//     },
//   },
//   {
//     name: {
//       officialName: "Analysis of Algorithms  3 cr  ",
//       shortName: "COMP 2080",
//       description:
//         "Methods of analyzing the time and space requirements of algorithms. Average case and worst case analysis.",
//     },
//   },
//   {
//     name: {
//       officialName: "Discrete Mathematics for Computer Science  3 cr  ",
//       shortName: "COMP 2130",
//       description:
//         "An introduction to the set theory, logic, integers, combinatorics and functions for today's computer scientists.",
//     },
//   },
// ];
// const createCourses = async () => {
//   //await Course.deleteMany();
//   const proc = courses.map(async (course) => {
//     const _course = new Course({
//       name: course.name,
//     });
//     await _course.save();
//   });

//   await Promise.all(proc);
// };

// export default createCourses;
