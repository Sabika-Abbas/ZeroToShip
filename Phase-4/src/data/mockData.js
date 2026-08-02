export const contacts = [
  {
    id: 1,
    name: "Sarah Johnson",
    organization: "Google",
    role: "Senior Software Engineer",
    email: "sarah.j@google.com",
    linkedin: "linkedin.com/in/sarahjohnson",
    status: "Keep in Touch",
    notes: [
      { date: "2026-07-28", text: "Met at Career Fair. She said they're hiring interns for summer." },
      { date: "2026-07-15", text: "Coffee chat – gave great advice on system design interviews." }
    ]
  },
  {
    id: 2,
    name: "Michael Chen",
    organization: "Microsoft",
    role: "Product Manager",
    email: "michael.c@microsoft.com",
    linkedin: "linkedin.com/in/michaelchen",
    status: "Overdue",
    notes: [
      { date: "2026-06-15", text: "Met at Hackathon. He was impressed with our project." }
    ]
  },
  {
    id: 3,
    name: "Aisha Khan",
    organization: "Amazon",
    role: "Data Scientist",
    email: "aisha.k@amazon.com",
    linkedin: "linkedin.com/in/aishakhan",
    status: "Keep in Touch",
    notes: [
      { date: "2026-07-25", text: "Guest lecture at university. She talked about AI in e-commerce." }
    ]
  },
  {
    id: 4,
    name: "David Park",
    organization: "Meta",
    role: "Frontend Engineer",
    email: "david.p@meta.com",
    linkedin: "linkedin.com/in/davidpark",
    status: "Overdue",
    notes: [
      { date: "2026-05-01", text: "Met at Tech Conference. He gave a talk on React performance." }
    ]
  }
];

export const getAIDraft = (contactId) => {
  const contact = contacts.find(c => c.id === contactId);
  if (!contact) return "Select a contact to generate a draft.";
  
  return `Hi ${contact.name},

I hope this message finds you well! I wanted to follow up on our recent conversation at the ${contact.organization} event. I really appreciated the insights you shared about ${contact.role} roles.

I've been working on some projects recently and would love to hear your thoughts if you have time for a quick coffee chat or call in the coming weeks.

Looking forward to staying connected!

Best regards,
[Your Name]`;
};